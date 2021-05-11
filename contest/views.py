from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
import uuid
from .models import *
from datetime import *
import random 
from django.utils import timezone

class GroferContest(viewsets.ViewSet):
    def generate_ticket(self, request,data = None):
        """creating ticket"""
        response={"success":True}
        user_id = request.data["user_id"]
        try:
            """check if user exist"""
            user_check = Users.objects.get(user_id = user_id)
            ticket = uuid.uuid1()
            p = Utc()
            p.user_id = user_id
            p.ticket = ticket
            p.save()
            response["ticket"] = ticket
        except:
            response["success"] = False
            response["message"] = "user does not exits"
        return Response(data = response, content_type="application/json")

    def take_part(self,request):
        response = {"success":False}
        user_id = request.data["user_id"]
        ticket = request.data["ticket"]
        contest = request.data["contest"]
        try:
            check1 = Utc.objects.get(user_id = user_id , contest = contest)
            response["message"] = "can not take part in the same contest again"
            return Response(data = response, content_type="application/json")
        except:
            pass
        try:
            contest_exist = All_Contests.objects.get(contest_name = contest)
        except:
            response["message"] = "Contest does not exist"
            return Response(data = response, content_type="application/json")
        try:
            check = Utc.objects.get(ticket = ticket)
            if check.contest:
                response["message"] = "ticket already used"
                return Response(data = response, content_type="application/json")
            if check.user_id != user_id:
                response["message"] = "ticket does not belongs to you"
                return Response(data = response, content_type="application/json")
            check.contest = contest
            check.save()
            response["success"] = True
        except:
            response["message"] = "ticket does not exist"
            return Response(data = response, content_type="application/json")
        
        return Response(data = response, content_type="application/json")

    def upcoming_event(self,request):
        """ making a query for all the next upcoming contest """
        startdate = datetime.today() - timedelta(hours = 10)
        enddate = startdate + timedelta(days=1)
        upcoming_events =All_Contests.objects.filter(end_date__range=(startdate, enddate))
        response = {}
        """iterating over all the contest we get from the query now storing them and there prize in response"""
        for upcoming_event in upcoming_events:
            response[str(upcoming_event.end_date)] = upcoming_event.contest_prize  
        return Response(data = response, content_type="application/json")

    def last_week_winners(self,request):
        response = {}
        startdate = datetime.today() - timedelta(days = 7)
        enddate = datetime.today() - timedelta(days =1)
        """ making a query for all the last weekk  contest """
        last_week_winners =All_Contests.objects.filter(end_date__range=[startdate, enddate])
        """iterating over all the last week contest """
        for last_week_winner in last_week_winners:
            """find the winner of this contest and putting it in the response dict """
            response[str(last_week_winner.contest_name)] = last_week_winner.winner  
        return Response(data = response, content_type="application/json")

    def find_winner(self,contests):
        for contest in contests:
            particepants = Utc.objects.filter(contest = contest.contest_name)
            """picking a random winner from all the user who took part """
            winner = random.choice(particepants)
            """making an object of contest table to store winner for the contest"""
            store_winner = All_Contests.objects.get(contest_name = winner.contest)
            """getting user information from user id from user table """
            user = Users.objects.get(user_id = winner.user_id)
            """storing the name of the winner in contest table """
            store_winner.winner = user.firstname + " " + user.lastname
            store_winner.save()
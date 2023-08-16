from flask import Blueprint, redirect, flash, session, render_template, url_for, request, jsonify
from firebase_admin import firestore
import datetime


configapp = Blueprint('configapp', __name__)




@configapp.app_template_filter('dtime')
def dtime(s):
    return s.strftime("%d/%m/%Y")


@configapp.app_template_filter('dettime')
def dettime(s):
    s = datetime.datetime.fromtimestamp(s.timestamp())
    return s.strftime("%d %b %Y")


@configapp.app_template_filter('detailtime')
def detailtime(s):
    s = datetime.datetime.fromtimestamp(s.timestamp())
    return s.strftime("%d %B %Y, %H:%M:%S")


@configapp.app_template_filter('detailtime1')
def detailtime1(s):
    s = datetime.datetime.fromtimestamp(s.timestamp())
    # return s.strftime("%d %B %Y, %H:%M")
    return s.strftime("%d %B %Y, %H:%M")


@configapp.app_template_filter('detailtime2')
def detailtime1(s):
    now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)
    s = datetime.datetime.fromtimestamp(s.timestamp())
    # waktu = s.strftime("%Y-%m-%d %H:%M:%S")
    return s.strftime("%Y-%m-%d %H:%M:%S")

    # return timeago.format(waktu, now, 'id_ID')


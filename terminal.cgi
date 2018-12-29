#!/usr/bin/python2
import cgi
import cgitb
import commands
cgitb.enable()
print "Content-type: text/html"
print ""
mypage_data=cgi.FieldStorage()

f_num=mypage_data.getvalue('x')
s_num=mypage_data.getvalue('y')
mycmd=mypage_data.getvalue('c')
#  adding numbers 
print  int(f_num)    +       int(s_num)
print   "<br/>"
print   "<pre>"
print   commands.getoutput('sudo  '+mycmd)
print "</pre>"
print "<h1>"
print "hello python with HTML"
print "<h1>"

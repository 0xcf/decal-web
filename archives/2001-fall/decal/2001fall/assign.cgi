#!/bin/sh
echo "Content-type: text/html"
echo
echo
echo "<HTML>"
echo "<title>CS198 Decal Project Completion</title>"
echo "<BODY>"
echo "username: "
whoami
echo "<BR>"
echo "uptime:&nbsp;&nbsp;&nbsp;&nbsp;"
uptime
echo "<HR>"
hostname
echo "<HR>"
date
echo "<HR>"
uname -a
echo "<HR>"
echo "</BODY>"
echo "</HTML>"

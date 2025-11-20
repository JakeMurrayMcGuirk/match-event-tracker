[1mdiff --git a/app/utils.py b/app/utils.py[m
[1mindex b99a865..11025a9 100644[m
[1m--- a/app/utils.py[m
[1m+++ b/app/utils.py[m
[36m@@ -42,6 +42,42 @@[m [mevent_shortcuts = {[m
     'f' : 'foul'[m
 }[m
 [m
[32m+[m[32mevent_categories = {[m[41m[m
[32m+[m[32m    'time' : ['begin game', 'end half', 'start half', 'end game'],[m[41m[m
[32m+[m[32m    'play' : ['shot', 'kickout', 'tackle', 'pass'],[m[41m[m
[32m+[m[32m    'foul' :  ['foul'][m[41m[m
[32m+[m[32m}[m[41m[m
[32m+[m[41m[m
[32m+[m[32mpossible_params = {[m[41m[m
[32m+[m[32m    'time' : 0,[m[41m[m
[32m+[m[32m    'begin game' : 0,[m[41m[m
[32m+[m[32m    'end half' : 0,[m[41m[m
[32m+[m[32m    'start half' : 0,[m[41m[m
[32m+[m[32m    'end game' : 0,[m[41m[m
[32m+[m[32m    'shot' : 3,[m[41m[m
[32m+[m[32m    'kickout' : 3,[m[41m[m
[32m+[m[32m    'tackle' : 2,[m[41m[m
[32m+[m[32m    'pass' : 2,[m[41m[m
[32m+[m[32m    'foul' : 1[m[41m[m
[32m+[m[32m}[m[41m[m
[32m+[m[41m[m
[32m+[m[32mparam_rules = {[m[41m[m
[32m+[m[32m    # Default ruleset[m[41m[m
[32m+[m[32m    'play' : {[m[41m[m
[32m+[m[32m        'outcome' : True,[m[41m[m
[32m+[m[32m        'player_no' : True[m[41m[m
[32m+[m[32m    },[m[41m[m
[32m+[m[32m    # Category rule for events in the time category[m[41m[m
[32m+[m[32m    'time' : {[m[41m[m
[32m+[m[32m        'outcome' : False,[m[41m[m
[32m+[m[32m        'player_no' : False[m[41m[m
[32m+[m[32m    },[m[41m[m
[32m+[m[32m    # Rule for fouls[m[41m[m
[32m+[m[32m    'foul' : {[m[41m[m
[32m+[m[32m        'outcome' : False,[m[41m[m
[32m+[m[32m        'player_no' : True[m[41m[m
[32m+[m[32m    }[m[41m[m
[32m+[m[32m}[m[41m[m
 [m
 outcomes = {[m
     'shot' : ['goal', 'point', '2 points', 'wide'],[m

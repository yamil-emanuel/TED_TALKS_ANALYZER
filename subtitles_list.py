
"""
INSTRUCTIONS:

DOWNLOADING TED TALK'S SUBTITLES:
I personally used youtube-dl
Running the following code in the terminal: youtube-dl --sub-lang es --write-auto-sub --sub-format srt [LINK-TO-THE-VIDEO]


PUTTING THEM INTO THE SCRIPT:
1)Using -ls command in terminal, copying all files-name
2)Pasting them into a variable called names

    names=''''Why people believe they can’t draw - and how to prove they can _ Graham Shaw _ TEDxHull-7TXEZ4tP06c.en.vtt'
    'Why we need to talk about suicide _ Mark Henick _ TEDxToronto-D1QoyTmeAYw.en.vtt'
    '''

3)Run the following code.
    final=[]
    names_l=(names.split('\n')[:-1])
    for name in names_l:
        if name[0]=="'" and name[-1]=="'":
            name=name.replace('"',"")
            final.append(name[1:-1])
        else:
            final.append(name)
    print(final)

4)Output will be:
    ['Why people believe they can’t draw - and how to prove they can _ Graham Shaw _ TEDxHull-7TXEZ4tP06c.en.vtt', 'Why we need to talk about suicide _ Mark Henick _ TEDxToronto-D1QoyTmeAYw.en.vtt']

5) Replace every ("') and ('") for ".

6)Subtitle's list is ready for being pasted into the subtitles_list tuple.

"""

#FORMAT "[NAME_OF_THE_VIDEO]-[URL].[LANG].vtt"
#USING DOUBLE (") IS MANDATORY FOR AVOIDING POSSIBLE CRASHES.


subtitles_list=[]

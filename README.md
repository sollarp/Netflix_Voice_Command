# Netflix_Voice_Command
This version runs on Raspberry Pi4B 4g using low quality USB MIC with HDMI out to Toshiba TV.

Netflix Voice Control(like Alexa or Google Assistant) using Picovoice and Google Cloud Speech_to_text API together for privacy reason with no cost 
apart from Netflix subscribe. 
Picovoice is a powerfull Wake word recognition software using little CPU and memory resources and runs offline.
-------------------------------------------------------------------------------------------------------------------------------------------
API used: 
 - Google cloud speechV1 (speech_to_text)
 - Google cloud speechV1 (text_to_speech)
 - snogs Netflix API (Rapid API)
 
 How to use:
 ###Sound##
 
 There is a configuration problem with sharing MIC on PI while running Picovoice and Google Cloud. This requires Alsamixer configuration on PI4.
 There is a possible bug in AlsaMixer so Google Speech to text through a "Invalide Sample rate issue" which noting to do with it just need to 
 run the following in Terminal "" arecord -f cd -c 1 -D dsnoop f333rt.wav" to test the MIC availability and run MAIN.py again.
 
 ###Chromium(Chrome)##
 
 Using Chrome Web driver with Selenium header to cheat Netflix. This could be difficult to achieve as need specific version.
 Noticed an issue with Web driver session for some reason after more than an hour flush out from memory. 
 
 ###Picovoice##
 
 This has 98% success rate recognizing wake word however in this case unrecognized command could lead to Google API to timeout stops program.
 Issue could be fixed to modify Google API library timing.
 
 
 Functionality:
 
 When "want to watch ......" command called the program try to find it in 3 different data base - 1st Local SQlite data base -
 - 2nd snogs Netflix Catalog -
 - 3rd Using Netflix search bar-
 Unfortunately the first 2 data bases have some disadvantages like not finding the right content or country restricted or none exist.

Requesting the show this could be stored by "add this to my playlist"
 
 
 Any question welcome if I can help...
 
 
 
 
 
 




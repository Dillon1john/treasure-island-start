print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
print(''' .. ........... .............  ........... . ..... ........ .......
 ......  ....................%.... .... ..... .........%............
 .@@@ ........ @@.... @@@@  . ............................  *  .....
 ....@@ ..... @ .... @ .............   ....... .....; .... *** .....
 .....\@\....@ .... @ ............................. #  .. *****  ...
  @@@.. @@@@@  @@@@@@___.. ....... ...%..... ...  {###}  *******
 ....@-@..@ ..@......@@@\...... %...... ....... <## ####>********
   @@@@\...@ @ ........\@@@@ ..... ...... ....... {###}***********
 ....%..@  @@ /@@@@@ . ....... ...............<###########> *******
 ...... .@-@@@@ ...V......     .... %.......... {#######}******* ***
 ...... .  @@ .. ..v.. .. . { } ............<###############>*******
 ......... @@ .... ........ {^^,     .......   {## ######}***** ****
 ..%..... @@ .. .%.... . .. (   `-;   ... <###################> ****
 . .... . @@ . .... .. _  .. `;;~~ ......... {#############}********
 .... ... @@ ... ..   /(______); .. ....<################  #####>***
 . .... ..@@@ ...... (         (  .........{##################}*****
 ......... @@@  ....  |:------( )  .. <##########################>**
  @@@@ ....@@@  ... _// ...... \\ ...... {###   ##############}*****
 @@@@@@@  @@@@@ .. / /@@@@@@@@@ vv  <##############################>
 @@@@@@@ @@@@@@@ @@@@@@@@@@@@@@@@@@@ ..... @@@@@@  @@@@@@@  @@@@
 @@@@@@###@@@@@### @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@###@##@@ @@@@@@@@@@@@@@@@@@@@@ @@@@@   @@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@### @@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@
 -@@@@@@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ''')
message = input(" You approach a diverging pathway. You can either go left or right, make your decision.\n").lower()

if message == "left":

    print('''                                        o
                             .-:"|
                             |-'"|
                                 |   _.-'`.
                                _|-"'_.-:|.`.
                               |:^.-:_:-'`:;.`.
                               |::.'.    ,- .=:|
                               |:::+.'-'_=:". J
            __.            .d88|:+:::+=: _-, .|
       _.--'_..`.    .d88888888|:||]:|, |:J].J8b.
    +:" ,--:_:|:.`.d88888888888|-' J:| .|:J|_|888b.
    |:\ \-'_.--'_.=+888888888+'  _-K:F.+:_   `88888bo.
     L:\ +'_.=='. .|88888+"'  _.'.J:J.J:::.    +8888888b.
     |:::+'. ._. . |8+"'  _.-', . |:| |::::+_   `+8888888._-'.
   .d8J::L. ./ \\ .J' _.-: . . . ,|:|.|::::::.,   `+888+'^.-|.`.
  d888|::| . F .FL J-'. . , . , . O:F F::::::/`/_ _.-"_.-:_:+::.`.
 d88888L::L .|::\L. L. . , . . . J:J J::::::/`/::|. +:_:-'    `;+ `;
 888888J::|. K:'  \.L . , . . _:-+:|.':::::/`/:::F::.`.     .-'_.=:J
 8888888|::L.L\    \|. . ._:-'     '   `::/`/:::J:::::.`..-'.='. . |
 8888888PL:| |:\    `._:-'               /`/::::|:|| \::..='. , . J.b
 8888888 |::L L:`.    \     _.-+.       /`/`::::L+`'  |::| . . , .F88b
 8888888  L:|.|:::\   _:.--'_.-|.`.    '`/   >-'     .J:J . , . .|8888b
 8888888  |::L.L:::+:" _.--:_:-'::.`.    _.-'    :"|':|:|. . . .JY88888b
 8888888   L:| |::::|\ \_:-'     `::.`.-'    :"|-'. .J:J. . , . F Y88888b
 Y888888    \:L L:::L:\ `.      _.-'_.=+ :"|-: . , . |:| , . , |   Y88888b
 `888888b    \|.|:::|:::. \ _.-'_.=: . |-', . . , . J:J . . . J     Y88888b
  Y888888     +'\:::J::::\ '_.='. . . .F . .,-T`\. .|:|. , ,-'      )888888
   Y88888b.      \:::L::::+. . , . . .J . ,/  |:O .J:J. ,-'        .d888888
    Y888888b      \::|::::| . . . , . |. . F  ::|,-'+|-'         .d88888888
     Y888888b      \:J::::|. . . . . .F , J .::-:              .od88888888P
      Y888888b      \:L:::| . , . , .J . .|::' ` \d8888888888888888888888P
       Y888888b      \|:::|. , . . , |. ,-'`.  `\ `+88888888888888888888P
        Y888888b.     J:::| . . , . .F-'     \\ ` \ \88888888888888888P'
         Y8888888b     L::|, . . , .J       d8+.`\  \`+8888888888888P'
          Y8888888b    |::| . , . ._+      d8888\  ` .'  `Y888888P'
          `88888888b   J::|. . ._-'     .od888888\.-'
           Y88888888b   \:| ._-'     d888888888P'              ,==. o
           `888888888b   \|-'       d88888888'                 |/ "'/L
            `Y88888888b            d8888888P'                 ,-_) '<_
              Y88888888bo.      .od88888888   hs               /^-._  \=_
              `8888888888888888888888888888                    `   (-'/ ~~
               Y88888888888888888888888888P                    a:f  | \
                `Y8888888888888888888888P'                          `  `
                  `Y8888888888888P'
                       `Y88888P'


 ''')
    message2 = input ("The left pathway leads to a castle surrounded by a moat of water.You can choose to swim past the moat or wait for a drawbridge. Will you swim or wait?\n").lower()
    if message2 == "wait":
        print('''
                                       /\
                                      /`:\
                                     /`'`:\
                                    /`'`'`:\
                                   /`'`'`'`:\
                                  /`'`'`'`'`:\
                                   |`'`'`'`:|
     _ _  _  _  _                  |] ,-.  :|_  _  _  _
    ||| || || || |                 |  |_| ||| || || || |
    |`' `' `' `'.|                 | _'=' |`' `' `' `'.|
    :          .:;                 |'-'   :          .:;
     \-..____..:/  _  _  _  _  _  _| _  _'-\-..____..:/
      :--------:_,' || || || || || || || `.::--------:
      |]     .:|:.  `' `'_`' `' `' `' `'    | '-'  .:|
      |  ,-. .[|:._     '-' ____     ___    |   ,-.'-|
      |  | | .:|'--'_     ,'____`.  '---'   |   | |.:|
      |  |_| .:|:.'--' ()/,| |`|`.\()   __  |   |_|.:|
      |  '=' .:|:.     |::_|_|_|\|::   '--' |  _'='.:|
      | __   .:|:.     ;||-,-,-,-,|;        | '--' .:|
      |'--'  .:|:. _  ; ||       |:|        |      .:|
      |      .:|:.'-':  ||       |;|     _  |]     _:|
      |      '-|:.   ;  ||       :||    '-' |     '--|
      |  _   .:|].  ;   ||       ;||]       |   _  .:|
      | '-'  .:|:. :   [||      ;|||        |  '-' .:|
  ,', ;._____.::-- ;---->'-,--,:-'<'--------;._____.::.`.
 ((  (          )_;___,' ,' ,  ; //________(          ) ))
  `. _`--------' : -,' ' , ' '; //-       _ `--------' ,'
       __  .--'  ;,' ,'  ,  ': //    -.._    __  _.-  -
   `-   --    _ ;',' ,'  ,' ,;/_  -.       ---    _,
       _,.   /-:,_,_,_,_,_,_(/:-\   ,     ,.    _
     -'   `-'--'-'-'-'-'-'-'-''--'-' `-'`'  `'`' `-SSt-
 ''')
        print("The drawbridge was lowered you shall proceed. ")
        message3 = input("You apprach room with 3 doors. A red door, a yellow door,and a blue door. Which color shall you choose?\n ").lower()
        if message3 == "yellow":
    
             print(''' ______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_| 
 ''')
             print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************\n\n"You win!! Room was filled treasure💰💰💰💰💰💰💰''')
        elif message3 == "red":
             print(''' ______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_| 
 ''')
             print('''     (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n Burnt by fire, Gameover.''') 
        elif message3 == "blue":
             print(''' ______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_| 
 ''')
             print('''   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/," \n\nSlayed by beast,Gameover.''')
        else:
            print("Wrong input, Gameover.")               
                        
    elif message2 == "swim":
        print('''                   _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
       jgs   ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~ \n\n Moat filled with crocodiles, Gameover. ''') 
    else:
        print("Wrong input, Gameover.")                       



elif message == "right":
  print("The right path is filled with quicksand,Game over.")
else:
  print("Wrong input, Gameover.")  




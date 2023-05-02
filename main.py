import hangman_words,hangman,random,pygame,hangman2

pygame.init() #module to initialize basic pygame functions
pygame.font.init() #module to type text on screen

#buttons
title_font = pygame.font.SysFont('Helvetica', 60)  #font to be used in game
button_font=pygame.font.SysFont('Arial', 25)
title_font2=pygame.font.SysFont('Comic Sans MS',50)
info_font=pygame.font.SysFont('Helvetica',30)

#basic background colours
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)

#screen size
width,height=800,600
window=pygame.display.set_mode((width,height))

#caption and icon
pygame.display.set_caption("Hangman")
icon=pygame.image.load("hangman pic.png")
pygame.display.set_icon(icon)

def title_screen():   #title screen vala text
    textsurface = title_font.render('Hangman', True, (0,0,0))
    window.blit(textsurface,(280,0))
    title_image=pygame.image.load("hangman pic.jpeg")
    window.blit(title_image,(250,200))

def lost_screen_button():
    pos=pygame.mouse.get_pos()
    if  260 <= pos[0] <= 460 and 435 <= pos[1] <= 475:     #button to play again
            pygame.draw.rect(window,blue,[260,435,200,40])
            
    else:
        pygame.draw.rect(window,green,[260,435,200,40])
    playagain=button_font.render("Play again",True,(0,0,0))
    window.blit(playagain,(265,440))
    if  260 <= pos[0] <= 460 and 520 <= pos[1] <= 560:     #button to exit
            pygame.draw.rect(window,blue,[260,520,200,40])
            
    else:
        pygame.draw.rect(window,green,[260,520,200,40])
    exit_button=button_font.render("EXIT",True,(0,0,0))
    window.blit(exit_button,(265,525))
    

def end_screen_won():
    running=True
    while running:
        window.fill(white)
        for ev in pygame.event.get():
            if ev.type==pygame.QUIT:
                pygame.quit()
            elif ev.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if 260<=pos[0]<=460 and 435<=pos[1]<=475:
                    return True
                elif 260<=pos[0]<=460 and 520<=pos[1]<=560:
                    pygame.quit()            
        won_text=title_font2.render("Congrats, You won",True,(0,0,0))
        window.blit(won_text,(90,150)) 
        lost_screen_button()
        pygame.display.update()
        

def end_screen_lost(word):
    running=True
    while running:
        window.fill(white)
        for ev in pygame.event.get():
            if ev.type==pygame.QUIT:
                pygame.quit()
            elif ev.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if 260<=pos[0]<=460 and 435<=pos[1]<=475:
                    return True
                elif 260<=pos[0]<=460 and 520<=pos[1]<=560:
                    pygame.quit()
        pos=pygame.mouse.get_pos()
        #showing user lost
        Text=title_font2.render("You lost",True,(0,0,0))
        window.blit(Text,(90,150))
        ##showing what the word was
        word_text=title_font2.render("The word was: "+word,True,(0,0,0))
        window.blit(word_text,(90,220))
        #dark souls reference
        gloat_text=title_font2.render("git gud ashen one",True,(0,0,0))
        window.blit(gloat_text,(90,280))
        #button to play again
        lost_screen_button()
        pygame.display.update()
        

def title_button():  #title screen button messsage
    butt_text=button_font.render('Start game',True,(0,0,0))
    window.blit(butt_text,(270,505))
    pygame.display.update()
    
def menutxt(): #menu heading and buttons message and image
    textsurface = title_font2.render('Difficulty', True, (0,0,0))
    window.blit(textsurface,(250,0)) 
    
    #easy button
    easy_but=button_font.render('EASY',True,(0,0,0))
    window.blit(easy_but,(65,155))
    
    #medium button
    medium_but=button_font.render('MEDIUM',True,(0,0,0))
    window.blit(medium_but,(65,275))
    
    #hard button
    hard_but=button_font.render('HARD',True,(0,0,0))
    window.blit(hard_but,(65,405))
    
    #exit button    
    exit_but=button_font.render('EXIT ',True,(0,0,0))
    window.blit(exit_but,(270,505))   
    
    #image
    title_image=pygame.image.load("hangman0.jpeg")
    window.blit(title_image,(400,200))
    
def gametxt(question):
    question_txt = title_font.render(question, True, (0,0,0))
    window.blit(question_txt,(250,100)) 
    len_question_txt=info_font.render("Word length: "+str(len(question)),True,(0,0,0))
    window.blit(len_question_txt,(550,40))
    
def game_picture(tries):
    img=pygame.image.load("hangman"+str(tries)+".jpeg")
    window.blit(img,(540,230))

def gamescreen(question,word): #gamescreen to display question and take answer
    runn=True
    name=""
    guess=""
    tries=0
    vowels=["a","e","i","o","u"]
    triesleft=6
    while runn:
        x=question
        guess=""
        window.fill(white)
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == pygame.K_RETURN:
                    guess=name
                    name = ""
            elif evt.type == pygame.QUIT:
                pygame.quit()
        gametxt(x )
        if guess in word and tries<6:
            question=hangman2.question_change(question,word,guess)
        elif guess not in word and tries<6 and guess not in vowels:
            tries+=1
            triesleft=6-tries
        tries_text=info_font.render("Number of tries left: "+str(triesleft),True,(0,0,0))
        window.blit(tries_text,(90,50))
        game_picture(tries)
        if tries==6:
            return [tries,word]
        elif question==word:
            return [tries,word]
        block=title_font.render(name, True, (0, 0, 0))    
        rect = block.get_rect()
        rect.center = window.get_rect().center
        window.blit(block, rect)
        pygame.display.flip()
            
    
    
def menu(): #runs after clicking start on title screen
    running=True
    while running:
        for ev in pygame.event.get():
            if ev.type==pygame.QUIT:
                running=False
            if ev.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if 265<=pos[0]<=465 and 500<=pos[1]<=540: #clicking exit button
                    pygame.quit()
                elif 60<=pos[0]<=260 and 150<=pos[1]<=190: #clicking esay button
                    word_set=hangman_words.easy.split('\n')
                    word=random.choice(word_set)
                    question=hangman.form_question(word)
                    return [question,word]
                elif 60<=pos[0]<=260 and 270<=pos[1]<=310: #clicking esay button
                    word_set=hangman_words.medium.split('\n')
                    word=random.choice(word_set)
                    question=hangman.form_question(word)
                    return [question,word]
                elif 60<=pos[0]<=260 and 400<=pos[1]<=440: #clicking esay button
                    word_set=hangman_words.hard.split('\n')
                    word=random.choice(word_set)
                    question=hangman.form_question(word)
                    return[question,word]
        window.fill(white)
        pos=pygame.mouse.get_pos()
        #button easy
        if  60<= pos[0] <=260 and 150<= pos[1] <=190:
            pygame.draw.rect(window,blue,[60,150,200,40])
            
        else:   
            pygame.draw.rect(window,green,[60,150,200,40])
        #button medium
        if  60 <= pos[0] <= 260 and 270 <= pos[1] <= 310:
            pygame.draw.rect(window,blue,[60,270,200,40])
            
        else:
            pygame.draw.rect(window,green,[60,270,200,40])
            
        # button hard
        if  60<= pos[0] <= 260 and 400 <= pos[1] <=440:
            pygame.draw.rect(window,blue,[60,400,200,40])
            
        else:
            pygame.draw.rect(window,green,[60,400,200,40])
        
        #exit button
        if  265<= pos[0] <=465 and 500 <= pos[1] <=540:
            pygame.draw.rect(window,blue,[265,500,200,40])
            
        else:
            pygame.draw.rect(window,green,[265,500,200,40])
        menutxt()    
        pygame.display.update()
    
def startscreen():   #starting screen to start the game
    run=True
    while run:
        for ev in pygame.event.get():
            if ev.type==pygame.QUIT:
                pygame.quit()
            if ev.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if 265<=pos[0]<=465 and 500<=pos[1]<=540:
                    x=menu()
                    return x
                    
        window.fill(white)
        pos=pygame.mouse.get_pos()
        if  265<= pos[0] <=465 and 500 <= pos[1] <=540:
            pygame.draw.rect(window,blue,[265,500,200,40])
            
        else:
            pygame.draw.rect(window,green,[265,500,200,40])
        textsurface = title_font.render('Hangman', True, (0,0,0))
        window.blit(textsurface,(280,0))
        title_image=pygame.image.load("hangman pic.jpeg")
        window.blit(title_image,(250,200))
        #button text 
        butt_text=button_font.render('Start game',True,(0,0,0))
        window.blit(butt_text,(270,505))
        pygame.display.update()
        
        
y=startscreen()
x=gamescreen(y[0],y[1])
if x[0]==6:
    var=end_screen_lost(x[1])
else:
    var=end_screen_won()
while var:
    y=startscreen()
    x=gamescreen(y[0],y[1])
    if x[0]==6:
        var=end_screen_lost(x[1])
    else:
        var=end_screen_won()
    

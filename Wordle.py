import pygame

pygame.init()
screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 90)
title_font = pygame.font.Font(None, 50)
title = title_font.render("Guess the word!", True, (255, 255, 255))
word_to_guess = "hello"
user_text = ""
results=[]
guesses = []
count=5
remain=True
#letter_surface = font.render("", True, (0, 0, 0))
while remain:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            remain=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]      # delete last character
            elif event.key == pygame.K_RETURN:
                if user_text:
                    colors = []
                    for i, letter in enumerate(user_text):
                        if i < len(word_to_guess):
                            if letter.lower() == word_to_guess[i]:
                                colors.append((0, 255, 0))  # green
                            elif letter.lower()  in word_to_guess:
                                colors.append((255, 255, 0))  # yellow
                            else:
                                colors.append((255, 0, 0))  # red
                        else:
                            colors.append((255, 0, 0))  # red for extra letters
                    guesses.append((user_text, colors))   # <-- add to it here
                    user_text = ""                # clear after Enter
            else:
                user_text += event.unicode      # add the typed character
    screen.fill("blue")
    screen.blit(title, (250, 10))
    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 600, 50))  # draw input box
    text_surface = font.render(user_text, True, ("black"))
    screen.blit(text_surface, (100, 100))
    for i, (guess, colors) in enumerate(guesses):
        for j, color in enumerate(colors):
            pygame.draw.rect(screen, color, (200 + j * 60, 200 + i * 60, 50, 57))
            letter_surface = font.render(guess[j].lower(), True, "black")
            screen.blit(letter_surface, (200 + j * 60, 200 + i * 60))        
    pygame.display.flip()  
    clock.tick(60)
pygame.quit()

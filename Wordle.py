import pygame

pygame.init()
screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 90)
guess_font = pygame.font.Font(None, 60)
title_font = pygame.font.Font(None, 50)
title = title_font.render("Guess the word!", True, (255, 255, 255))
word_to_guess = "HELLO"
user_text = ""
results=[]
guesses = []
count=5 # list of remaining guesses
remain=True
count_surface = guess_font.render("Guesses remaining: " + str(count), True, (255, 255, 255))
while remain:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            remain=False
        if event.type == pygame.KEYDOWN and count>0:  # only process input if guesses remain
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]      # delete last character
            elif event.key == pygame.K_RETURN:
                count -= 1
                count_surface = guess_font.render("Guesses remaining: " + str(count), True, (255, 255, 255))
                if user_text:
                    colors = []
                    for i, letter in enumerate(user_text):
                        if i < len(word_to_guess):
                            if letter.upper() == word_to_guess[i]:
                                colors.append((0, 255, 0))  # green
                            elif letter.upper()  in word_to_guess:
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
    screen.blit(count_surface, (150, 45))  # display remaining guesses
    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 600, 50))  # draw input box
    text_surface = font.render(user_text.upper(), True, ("black"))
    screen.blit(text_surface, (100, 100))
    for i, (guess, colors) in enumerate(guesses):
        for j, color in enumerate(colors):
            pygame.draw.rect(screen, color, (200 + j * 60, 200 + i * 60, 50, 57))
            letter_surface = font.render(guess[j].upper(), True, "black")
            screen.blit(letter_surface, (200 + j * 60, 200 + i * 60))
    if count==0:  # if no guesses left
                panel = pygame.Surface((400, 400))  # create a panel surface
                panel.fill((200, 40, 40))
                game_over_font = pygame.font.Font(None, 40)
                game_over_text = game_over_font.render("Game Over!", True, (255, 255, 255))
                panel.blit(game_over_text, game_over_text.get_rect(center=(panel.get_width() // 2, 80)))  # center the text horizontally
                correct_word_text = game_over_font.render(f"The correct word was: {word_to_guess.upper()}", True, (255, 255, 255))
                panel.blit(correct_word_text, correct_word_text.get_rect(center=(panel.get_width() // 2, 160)))  # center the text horizontally
                screen.blit(panel, panel.get_rect(center=screen.get_rect().center))        
    pygame.display.flip()  
    clock.tick(60)
pygame.quit()

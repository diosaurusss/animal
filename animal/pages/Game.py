import streamlit as st
import pygame

pygame.init()

st.title("Streamlit Game")

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 0, 0))
    
    # Draw your game elements here
    
    pygame.display.update()
    
pygame.quit()

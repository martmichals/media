import re
import math
from manim import *
import numpy as np

class Definition(Scene):

    def construct(self):
        # Scene constants
        font_size = 40
        font = 'sans-serif'

        # Texts
        question = Text(
            'What is Natural Language Processing?',
            font_size=font_size, font=font
        )

        text = Text(
            """
            \"Natural language processing strives 
            to build machines that understand 
            and respond to text or voice data—and 
            respond with text or speech of their 
            own—in much the same way humans do.\"
            """,
            font=font, font_size=font_size
        )

        author = Text(
            '- IBM',
            font=font, font_size=font_size, slant=ITALIC
        )
        author.next_to(text, DOWN).align_to(text, RIGHT)

        # Question
        self.play(Write(question))
        self.wait(1)

        # Definition
        self.play(
            Transform(question, text), run_time=2
        )
        self.play(Write(author))
        self.wait(1)

        # Point of focus
        # TODO Change color to something that pops
        self.play(
            text[74:78].animate.set_color(GREEN)
        )

import re
import math
from manim import *
import numpy as np

class Logo(Scene):
    def construct(self):
        # Define texts
        title = Text('EnigmaText', weight='LIGHT', font_size=125)
        subtitle = Text('Natural language processing, simplified.', font_size=25).shift(DOWN)

        # Write channel logo to screen
        self.wait(0.25)
        self.play(Write(title, run_time=1.25)) 
        self.play(Write(subtitle, run_time=1)) 
        self.wait()
        
        # Wipe the screen
        self.play(
            Unwrite(subtitle, run_time=0.75), 
            Unwrite(title, run_time=0.75)
        )
        self.wait(0.10)

SPACES_TO_INSERT = 10
class SimpleTokenizationExample(Scene):
    def construct(self):
        # Sample text
        sent_text = 'I got groceries from the store.'
        sent = Text(sent_text, font_size=30)

        # Space out the tokens
        sent_split_text = sent_text.replace(' ', ' '*SPACES_TO_INSERT)
        sent_split = Text(sent_split_text, font_size=30)

        # Write the sample to the screen
        self.play(Write(sent))
        # self.wait(0.5)

        # Send to the top of the screen
        self.play(sent.animate.to_edge(UP))
        # self.wait()

        # Indices of spaces in the original sentence
        space_indices = [(m.end()-m.start()-1)/2 + m.start() for m in re.finditer(r'\w+', sent_text)]
        space_indices = [(math.floor(idx), math.ceil(idx)) for idx in space_indices]

        # Compute start coordinates for arrows
        arrow_starts = [
            np.array([
                sent[idx[0]-idxnum].get_bottom(), 
                sent[idx[1]-idxnum].get_bottom()
            ]).mean(0)
        for idxnum, idx in enumerate(space_indices)]
        arrow_ends = [
            np.array([
                sent_split[idx[0]-idxnum].get_top(), 
                sent_split[idx[1]-idxnum].get_top()
            ]).mean(0)
        for idxnum, idx in enumerate(space_indices)]

        # Plot the tokenized sentence
        arrows = [
            Arrow(
                start=s, 
                end=e, 
                buff=0.2, 
                max_tip_length_to_length_ratio=0.06,
                max_stroke_width_to_length_ratio=1
            ) 
        for s, e in zip(arrow_starts, arrow_ends)]
        self.play(Create(VGroup(*arrows)), Write(sent_split))
        self.play(Uncreate(VGroup(*arrows)))
        # self.wait()

        # Highlight the good portion of the sentence
        self.play(
            sent_split[:20].animate.set_color(GREEN),
            sent_split[20:].animate.set_color(RED)
        )

class TokenizationExampleWithPunc(Scene):
    def construct(self):
        # Sample text
        sent_text = 'I got groceries from the store.'
        sent = Text(sent_text, font_size=30)

        # Space out the tokens
        sent_text = 'I got groceries from the store .'
        sent_split_text = sent_text.replace(' ', ' '*SPACES_TO_INSERT)
        sent_split = Text(sent_split_text, font_size=30)

        # Write the sample to the screen
        self.play(Write(sent))
        # self.wait(0.5)

        # Send to the top of the screen
        self.play(sent.animate.to_edge(UP))
        # self.wait()

        # Indices of spaces in the original sentence
        space_indices = [(m.end()-m.start()-1)/2 + m.start() for m in re.finditer(r'\w+', sent_text)]
        space_indices = [(math.floor(idx), math.ceil(idx)) for idx in space_indices]

        # Compute start coordinates for arrows
        arrow_starts = [
            np.array([
                sent[idx[0]-idxnum].get_bottom(), 
                sent[idx[1]-idxnum].get_bottom()
            ]).mean(0)
        for idxnum, idx in enumerate(space_indices)]
        arrow_ends = [
            np.array([
                sent_split[idx[0]-idxnum].get_top(), 
                sent_split[idx[1]-idxnum].get_top()
            ]).mean(0)
        for idxnum, idx in enumerate(space_indices)]

        # Plot the tokenized sentence
        arrows = [
            Arrow(
                start=s, 
                end=e, 
                buff=0.2, 
                max_tip_length_to_length_ratio=0.06,
                max_stroke_width_to_length_ratio=1
            ) 
        for s, e in zip(arrow_starts, arrow_ends)]
        self.play(Create(VGroup(*arrows)), Write(sent_split))
        self.play(Uncreate(VGroup(*arrows)))
        # self.wait()

        # Highlight the good portion of the sentence
        self.play(sent_split.animate.set_color(GREEN))


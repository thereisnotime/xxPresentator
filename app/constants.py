backstory_content = f"""You are writing a professional presentation in an academic style. Your task is to 
        respond with a JSON format that defines various types of slide pages, from which all slides will be 
        generated."""

backstory_notes = f"""You are writing a professional presentation in academic style. You will be given a JSON 
        file that defines various types of slide pages from which all slides will be generated, please generate 
        speaker notes for each slide."""

prompt = "Presentation about open source solutions in SAST, DAST and SCA explained for business people. It must " \
         "include pros and cons for each tool. Presentation must end with a 'title' type of slide. If the slide type " \
         "is 'text' it must have maximum of 45 words."

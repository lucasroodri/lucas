from google import genai
from google.genai import types

cliente = genai.Client(api_key="ID_API")



class AnalizadorDeSentimientos():
    def analizar_sentimientos(self, polaridad):
        if polaridad > -0.6 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[1;37m"
        elif polaridad > -0.3 and polaridad <= -0.1:
            return "\x1b[1;31m" + "Algo Negativo" + "\x1b[1;37m"
        elif polaridad > -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[1;37m"
        elif polaridad > 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo Positivo" + "\x1b[1;37m"
        elif polaridad > 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[1;37m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy Positivo" + "\x1b[1;37m"
        else:
            return "\x1b[1;31m" + "Muy Negativo" + "\x1b[1;37m"


analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "\nDime algo: " + "\x1b[1;37m")

    if user_prompt.lower() == "salir":
        break

    contents = user_prompt

    response = cliente.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction="""
            Eres un chatbot especializado en analizar sentimientos.

            Debes analizar el sentimiento del texto recibido y responder
            únicamente con un número entre -1 y 1.

            -1 = negatividad máxima
             0 = neutral
             1 = positividad máxima

            Puedes utilizar números enteros o decimales.
            No escribas absolutamente nada más.
            """
        )
    )

    polaridad = float(response.text)

    resultado = analizador.analizar_sentimientos(polaridad)
    print(resultado)
from google import genai
from google.genai import types

cliente = genai.Client(api_key="ID_API")


class Sentimiento():
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return "\x1b[1;{}m\x1b[1;{}m".format(self.color, self.nombre) #.format() reemplazará el 1º {} por color y el 2º por nombre

class AnalizadorDeSentimientos():
    def __init__(self, rangos):
        self.rangos = rangos

    def analizar_sentimientos(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return ("Muy Negativo", "31")


rangos = [
    ((-0.6,-0,3), Sentimiento("Negativo","31")),
    ((-0.3,-0,1), Sentimiento("Algo Negativo","31")),
    ((-0.1,0,1), Sentimiento("Neutral","33")),
    ((0.1,0,4), Sentimiento("Algo Positivo","32")),
    ((0.4,0,8), Sentimiento("Positivo","32")),
    ((0.8,1), Sentimiento("Muy Positivo","32"))
]


analizador = AnalizadorDeSentimientos(rangos)

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
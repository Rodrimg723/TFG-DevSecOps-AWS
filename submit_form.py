# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import random
import time
import sys

# Action URL
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSddH54enUmKHQMj43QplwAmUbl_Ztmgy2c-y33NyM8KvXA06A/formResponse"

# Tokens
FBZX = "9203316303287658143"

# Questions
QUESTIONS = [
    # Age (Required)
    { "id": "entry.1535955828", "type": "choice", "options": ['Menos de 18 años', '18 - 25 años', '26 - 50 años', 'Más de 50 años'] },
    # Gender (Required)
    { "id": "entry.1395942463", "type": "choice", "options": ['Masculino', 'Femenino'] },
    # Gym Status (Required)
    { "id": "entry.1985576436", "type": "choice", "options": ['Voy al gimnasio/hago deporte 3 o más veces por semana', 'Estoy apuntado pero voy muy poco (menos de lo que me gustaría)', 'Me he borrado o he dejado de ir recientemente', 'Nunca me apunto porque sé que no iré'] },
    # Reasons (Required)
    { "id": "entry.2082771363", "type": "checkbox", "options": ['Falta de tiempo real (trabajo/estudios)', 'Aburrimiento / Me da pereza ir solo', 'Dinero (es muy caro)', 'Vergüenza / Me siento intimidado por el ambiente o las máquinas', 'Falta de resultados rápidos'] },
    # Laziness (Required)
    { "id": "entry.1541982119", "type": "scale", "min": 1, "max": 5 },
    # App help (Required)
    { "id": "entry.1215676183", "type": "choice", "options": ['Sí, definitivamente. El compromiso con otra persona me obliga a ir', 'Tal vez, dependería de quién sea la persona', 'No, prefiero entrenar solo/a con mis auriculares', 'No, mi problema es la falta de tiempo, no la compañía'] },
    # Worries (Required)
    { "id": "entry.1491264429", "type": "checkbox", "options": ['La seguridad (quedar con un desconocido)', 'Que la otra persona tenga un nivel muy diferente al mío (me frene o me canse)', 'Que se use para ligar en vez de para entrenar', 'Que la otra persona me falle y no aparezca', 'Nada, me parece una idea genial sin peros'] },
    # Filter (Required)
    { "id": "entry.1328468896", "type": "checkbox", "options": ['Que sea de mi mismo género', 'Que tenga mi misma edad', 'Que vaya exactamente a mi mismo gimnasio', 'Que tenga mi mismo nivel'] },
    # Payment (Required)
    { "id": "entry.1308553846", "type": "choice", "options": ['Gratis total (con anuncios)', 'Pagaría un pequeño precio único (ej. 2€) por verificar mi cuenta y usarla siempre', 'Pagaría una suscripción mensual baja (ej. 3€/mes) por funciones premium', 'No pagaría nada bajo ningún concepto'] },
    # Free Gym (Required)
    { "id": "entry.2025457450", "type": "choice", "options": ['Sí, deberían facilitar que nos conozcamos', 'No, es cosa mía'] },
    # Recommend (Required)
    { "id": "entry.103527756", "type": "scale", "min": 0, "max": 10 },
    # Feed Look (Not Required) - But choice
    { "id": "entry.2078711036", "type": "choice", "options": ['Si', 'No'] },
    # Feed Feedback (Not Required)
    { "id": "entry.1933222992", "type": "text", "required": False },
    # Suggestions (Required)
    { "id": "entry.266652913", "type": "text", "required": True }
]

TEXT_RESPONSES = ["Me parece buena idea", "Interesante", "Nada que añadir", "Muy útil", "Ojalá salga pronto", "Buena iniciativa", "Ninguna", "Ok", "."]

def submit_response(index):
    data = []
    
    # Standard hidden fields
    data.append(('fbzx', FBZX))
    data.append(('fvv', '1'))
    data.append(('pageHistory', '0'))
    
    for q in QUESTIONS:
        key = q["id"]
        
        if q["type"] == "choice":
            valid_opts = [o for o in q["options"] if o.strip()]
            val = random.choice(valid_opts)
            data.append((key, val))
            
        elif q["type"] == "checkbox":
            valid_opts = [o for o in q["options"] if o.strip()]
            count = random.randint(1, min(3, len(valid_opts)))
            selected = random.sample(valid_opts, count)
            for s in selected:
                data.append((key, s))
                
        elif q["type"] == "scale":
            val = str(random.randint(q["min"], q["max"]))
            data.append((key, val))
            
        elif q["type"] == "text":
            required = q.get("required", False)
            if required:
                # Always provide text
                val = random.choice(TEXT_RESPONSES)
            else:
                if random.random() < 0.2:
                    val = random.choice(TEXT_RESPONSES)
                else:
                    val = ""
            data.append((key, val))
            
    # Encode
    payload = urllib.parse.urlencode(data)
    binary_data = payload.encode('utf-8')
    
    req = urllib.request.Request(FORM_URL, data=binary_data)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print(f"[{index}] Submitted OK.")
            else:
                print(f"[{index}] Failed: {response.status}")
    except Exception as e:
        print(f"[{index}] Error: {e}")
        # Print error body if possible
        try:
             # For urllib.error.HTTPError
             if hasattr(e, 'read'):
                 print(e.read().decode('utf-8'))
        except:
            pass

if __name__ == "__main__":
    count = 1
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
        
    print(f"Running {count} submissions...")
    for i in range(count):
        submit_response(i+1)
        if count > 1:
            time.sleep(random.uniform(0.5, 2.0))

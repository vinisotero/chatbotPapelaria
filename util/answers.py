from twilio.twiml.messaging_response import MessagingResponse
from flask import request
from util import db

# Dicionário de opções de atendimento


def firstAnswer():

    respostas = ('1','atacado', 'vendas em atacado', '2', 'vendas em varejo', 'varejo', '3', 'setor de compras', 'compras', '4', 'gerencia', 'gerência', '5', 'sac')

    incoming_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg in respostas:
        if incoming_msg == respostas[0] or incoming_msg == respostas[1] or incoming_msg == respostas[2]: #atacado
            destinatario = db.atual_destinatario(1)
        elif incoming_msg == respostas[3] or incoming_msg == respostas[4] or incoming_msg == respostas[5]: #varejo
            destinatario = db.atual_destinatario(2)
        elif incoming_msg == respostas[6] or incoming_msg == respostas[7] or incoming_msg == respostas[8]: #compras
            destinatario = db.atual_destinatario(3)
        elif incoming_msg == respostas[9] or incoming_msg == respostas[10] or incoming_msg == respostas[11]:#gerencia
            destinatario = db.atual_destinatario(4)
        else:#sac
            destinatario = db.atual_destinatario(5)
        
        destinatario_whatsapp_link = f"https://wa.me/55{destinatario}"
        
        # Use HTML para criar um botão clicável
        msg.body("Você escolheu a opção {}. Clique no link abaixo para iniciar uma conversa com um de nossos atendentes:".format(incoming_msg))
        msg.body(destinatario_whatsapp_link)
        msg.body('Obrigado por procurar o Armazém de Papelaria')

    else:
        msg.body('Olá, Seja bem-vindo ao Armazém de Papelaria, eu estou aqui para ajudar você com todas as suas dúvidas e necessidades. Para proporcionar a melhor assistência possível, oferecemos suporte em diversas categorias. Por favor, Digite o número de qual atendimento deseja:\n1. Vendas em Atacado \n2. Vendas em Varejo \n3. Setor de Compras \n4. Gerência \n5. SAC')

    return str(resp)
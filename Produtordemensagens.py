import pika

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaração da fila
channel.queue_declare(queue='pedido_loja_online')

# Simulação de pedidos da loja online
pedidos = [
    "Pedido1",
    "Pedido2",
    "Pedido3"
]

# Envia os pedidos para a fila
for pedido in pedidos:
    channel.basic_publish(exchange='',
                          routing_key='pedido_loja_online',
                          body=pedido)
    print(f"Pedido '{pedido}' enviado para a fila")

connection.close()

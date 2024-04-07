import pika

# Callback para enviar os pedidos processados para o sistema de envio
def callback(ch, method, properties, body):
    pedido = body.decode()
    print(f"Pedido processado: {pedido}")

    # Simulação do envio do pedido para o sistema de envio/logística
    # Aqui você deve implementar a lógica real de integração com o sistema de envio/logística

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaração da fila
channel.queue_declare(queue='pedido_envio_logistica')

# Consumo de mensagens
channel.basic_consume(queue='pedido_envio_logistica', on_message_callback=callback, auto_ack=True)

print('Aguardando pedidos processados...')
channel.start_consuming()

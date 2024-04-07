import pika
import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

# Criação da tabela de pedidos
cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   pedido TEXT)''')

# Callback para processar os pedidos recebidos
def callback(ch, method, properties, body):
    pedido = body.decode()
    print(f"Pedido recebido: {pedido}")

    # Processamento e registro do pedido no banco de dados
    cursor.execute("INSERT INTO pedidos (pedido) VALUES (?)", (pedido,))
    conn.commit()
    print("Pedido registrado no banco de dados")

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaração da fila
channel.queue_declare(queue='pedido_loja_online')

# Consumo de mensagens
channel.basic_consume(queue='pedido_loja_online', on_message_callback=callback, auto_ack=True)

print('Aguardando pedidos...')
channel.start_consuming()

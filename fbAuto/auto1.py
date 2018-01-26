import facebook

my_token = ""
with open('matruycap', 'r') as textfile:
     my_token = textfile.readline()

# print(my_token)
graph = facebook.GraphAPI(access_token=my_token)
args = {'fields' : 'message'}
# post = graph.get_object(id="10159809967065704", fields='message')
# print(post['message'])
profile = graph.get_object("me")
posts = graph.get_connections(id="me", connection_name="likes")
print(posts)
for post in posts['data']:
    print(post['name'], "-", post['id'])
# inb =
mess = graph.request('me/inbox')
print(mess)
# for post in posts['data']:
#     try:
#         print(post['id'])
#         graph.put_object(parent_object=post['id'], connection_name='likes')
#         graph.put_like(object_id=post['id'])
#         print("Liking the topic:", post['message'])
#     except:
#         continue
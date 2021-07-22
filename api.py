import requests
import json
import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email, password):

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo):

        data = MultipartEncoder
        fields={
                'name' : name,
                'age' : age,
                'animal_type' : animal_type,
                'pet_photo' : (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            }
        headers = {'auth_key' : auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', data=data, headers=headers)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def delete_pet(self, auth_key: json, pet_id: str):

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + f' /api/pets/{pet_id}', headers=headers)
        status = res.status_code

        return status

    def add_photo_pet(self, auth_key: json, pet_id: str, pet_photo):

        data = MultipartEncoder(
        fields={
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        })

        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + f'/api/pets/set_photo/{pet_id}', data=data, headers=headers)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except:
            result = res.text

        return  status, result

    def list_pets(self, auth_key: json, filter: str = ''):

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text

        return status, result






from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from faker import Faker
import hashlib

from cms.models import Media
from .setup import admin_user_setup


class MediaModelTest(TestCase):

    def setUp(self):
        self.admin_user = admin_user_setup()
        self.BUFFER_SIZE = 65536  # Hash chunk size

    def test_media_created(self):
        faker = Faker('en_US')
        md5 = hashlib.md5()
        with open('./test_media/2954199.jpg', 'rb') as f:
            while True:
                data = f.read(self.BUFFER_SIZE)
                if not data:
                    break
                md5.update(data)

        test_media = Media(
            title=faker.sentence(nb_words=4),
            description=faker.paragraph(nb_sentences=3),
            media_file=SimpleUploadedFile(name=md5.hexdigest() + '.jpg',
                                          content=open(
                './test_media/2954199.jpg', 'rb').read(),
                content_type='image/jpeg'), instance=self.admin_user.id
            UserProfile=self.admin_user
        )
        test_media.save()

import hashlib
import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from faker import Faker

from cms.models import Media

from .setup import admin_user_setup


class MediaModelTest(TestCase):

    def setUp(self):
        self.admin_user = admin_user_setup()
        self.BUFFER_SIZE = 65536  # Hash chunk size

    def test_media_created(self):
        faker = Faker('en_US')
        md5 = hashlib.md5()
        with open(os.getcwd() + '/cms/tests/test_media/2954199.jpg', 'rb') as f:
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
                                              os.getcwd() + '/cms/tests/test_media/2954199.jpg', 'rb')
                                          .read(),
                                          content_type='image/jpeg'),
            UserProfile=self.admin_user
        )
        test_media.save()
        self.assertEqual(test_media.media_file.name, md5.hexdigest() + '.jpg')
        test_media.delete_media_file()

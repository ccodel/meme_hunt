from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

def standard_page_test(test, url, template, view):
   # Verify status code
   test.assertEqual(test.response.status_code, 200)
   
   # Verify template used
   test.assertTemplateUsed(test.response, template)

   # Verify resolves to view
   resolved_view = resolve(url)
   test.assertEqual(resolved_view.func.__name__, view.as_view().__name__)

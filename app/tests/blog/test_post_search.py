import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


pytestmark = pytest.mark.django_db


class TestPostSearch:
    def test_search_url(self, client, post_factory):
        url = reverse("post_search")
        response = client.get(url)
        assert response.status_code == 200

    def test_search_htmlx_fragment(self, client, post_factory):
        headers = {"HTTP_HX-Request": "true"}
        url = reverse("post_search")
        response = client.get(url, **headers)
        assertTemplateUsed(response, "blog/components/post-list-elements-search.html")

    def test_search_filter(self, client, post_factory):
        post = post_factory(title="test")
        url = reverse("post_search")
        request = f"{url}?search_field={post.title}"
        response = client.get(request)
        assert post.title in response.context["posts"][0].title
        # assert post.title in response.content.decode("utf-8") # also possible to use the whole content
        # to see output use: pytest -rR ( ? similar to pytest -s)
        print(response.content)

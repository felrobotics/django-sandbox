import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


pytestmark = pytest.mark.django_db


class TestListbyTag:
    def test_tag_url(self, client, post_factory):
        post_factory(title="test-post", tags=["test-tag"])
        url = reverse("post_by_tag", kwargs={"tag": "test-tag"})
        response = client.get(url)
        assert response.status_code == 200

    def test_htmlx_fragment(self, client, post_factory):
        post_factory(title="test-post", tags=["test-tag"])
        url = reverse("post_by_tag", kwargs={"tag": "test-tag"})
        headers = {"HTTP_HX-Request": "true"}
        response = client.get(url, **headers)
        assertTemplateUsed(response, "blog/components/post-list-elements-tags.html")

    def test_tag_filter(self, client, post_factory):
        post = post_factory(title="test-post", tags=["test-tag"])
        url = reverse("post_by_tag", kwargs={"tag": "test-tag"})
        response = client.get(url)
        assert post.tags.all()[0].name == response.context["tag"]

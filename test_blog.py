import pytest
from unittest.mock import Mock, patch
from blog import Blog

api_response_3 = [
    {'userId': 5, 'id': 5, 'title': 'Mais um Titulo 1', 'body': 'Mais um Conteudo do blog 1'},
    {'userId': 6, 'id': 6, 'title': 'Mais um Titulo 2', 'body': 'Mais um Teste de conteudo do blog 2'}
]

@pytest.fixture
def mock_requests_get_3():
    with patch('blog.requests.get') as mock_get:
        yield mock_get

@pytest.fixture
def blog_instance_3(mock_requests_get_3):
    mock_requests_get_3.return_value.json.return_value = api_response_3
    return Blog()

def test_posts_3(blog_instance_3):
    result = blog_instance_3.posts()
    assert result == api_response_3

def test_post_by_user_id_3(blog_instance_3, mock_requests_get_3):
    mock_requests_get_3.return_value.json.return_value = api_response_3[0]
    result = blog_instance_3.post_by_user_id(5)
    assert result == api_response_3[0]


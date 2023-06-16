            <!-- Add/Remove from favorites button -->
            <!-- <form method="POST" action="{% url 'favourite_film' film.id %}">
              {% csrf_token %}
              <button type="submit" class="btn btn-primary">
                {% if film in request.user.favorite_films.all %}
                  Remove from Favorites
                {% else %}
                  Add to Favorites
                {% endif %}
              </button>
            </form> -->
**Usage**
=========
| Usage for the library apex_stats

| Before using this library make sure you use 

.. code-block :: python

    import apex_stats

not

.. code-block :: python

    import apex-stats

*recentlyPlayed(username/id, userplatform)*
#####################################################

| Returns 5 of your recently played legends as a list.

| **username/id** - the desired username to get data from.

| **userplatform** -  default=origin, choose from 'origin', 'xbl', 'psn'.

.. code-block:: python
   :linenos:


    apexInstance = apex.recentlyPlayed(your-tracker.gg-api-key)
    apexStats = apexInstance.recentlyPlayed("testuser")

    print(apexStats)

    >>> ['your', 'last', 'played', 'characters']


*matchHistory(username/id, gamecount, userplatfom)*
#####################################################

| Returns data from x number of games.

| **username/id** - the desired username to get data from.

| **userplatform** -  default=origin, choose from 'origin', 'xbl', 'psn'.

| **gamecount** - number of games you want data from (counted from your last game)

.. code-block:: python
   :linenos:

    apexInstance = apex.recentlyPlayed(your-tracker.gg-api-key)
    apexHistory = apexInstance.matchHistory("testuser", 2)

    print(apexStats)

    >>> [{game1:legend, game1:kills, game1:duration},
    {game2:legend, game2:kills, game2:duration}]

B
    �Ԑ`  �               @   s   d dl Zdd� ZdS )�    Nc             C   s�   t �| �at�d�at�d�at�d�at jttdddd�at jttdddd�atj t�	� }|d	 d d
� a
td	 j�dd�td	< td �� dd� atd dk}t| d	dg add l}|�d� td dkatt ad S )NZimdbZ	directorsZ	countries�innerZ
country_id�id)�left�rightZhowZleft_onZright_onZdirector_idZmovie_title�
   �   Ê� Zdirector_namer   �   zChristopher NolanZ
imdb_scoreg������ @)�pdZ	ExcelFileZxls�parseZdfZdf_directorsZdf_countries�merge�shape�copyZfirst10�str�replaceZvalue_countsZdirector_with_mostZall_movies_ratings�randomZseedZ	goodmovieZpossible_goodmovies)�filepathZdf_copyZnolanr   � r   �./home/jovyan/work/source/Module 7/solutions.py�get_solutions   s*    







r   )Zpandasr
   r   r   r   r   r   �<module>   s   
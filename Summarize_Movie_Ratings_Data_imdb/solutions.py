B
    �O_8  �               @   s   d dl Zdd� ZdS )�    Nc             C   s  t �| �at�d�at�d�at�d�at jttdddd�at jttdddd�at��  d	d
ga	tt	 �� a
td dkatt d	 �� at�d�d	 �� atd dk}td dk}td dk}t|||@ @  add l}t jtddgd	g|jgd�at ttd dk d ad S )NZimdb�	directorsZ	countries�innerZ
country_id�id)�left�rightZhowZleft_onZright_onZdirector_idZ
imdb_scoreZgrossZdirector_namezChristopher Nolan�   Z
title_yeari�  �.   r   Zcountry)�index�valuesZaggfuncZmovie_titleZ	GladiatorZduration)�pdZ	ExcelFileZxls�parseZdfZdf_directorsZdf_countries�mergeZdescribeZscore_grossZscore_gross_descriptionZnolanZmeanZ
nolan_mean�groupbyr   ZmiyazakiZnumpyZpivot_tableZmedianZ	pivot_aggZgladiator_duration)�filepathZnot_usaZbefore_1960ZMiyazakiZnp� r   �./home/jovyan/work/source/Module 8/solutions.py�get_solutions   s2    








r   )Zpandasr   r   r   r   r   r   �<module>   s   
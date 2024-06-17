class Node:
    def __init__(self, titulo, autor, paginas, proximo) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.proximo = proximo
    
    def __str__(self) -> str:
        return f"Título: {self.titulo}; Autor: {self.autor}; Páginas: {self.paginas}"
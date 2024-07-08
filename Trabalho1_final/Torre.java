package trabalho.Trabalho1_Java;

public class Torre {
    public int id;
    public String nome;
    public String endereco;

    public Torre(int id, String nome, String endereco){
        this.id = id;
        this.nome = nome;
        this.endereco = endereco;
    }

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public String toString(){
        return "ID. Torre: " + id + ", Nome: " + nome + ", Endereco: " + endereco;
    }
}

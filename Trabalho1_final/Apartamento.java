package trabalho.Trabalho1_Java;

public class Apartamento {
    private int id;
    private int num;
    private Torre torre;
    private int vaga;

    public Apartamento(int id, int num, Torre t,int vaga){
        this.id = id;
        this.num = num;
        this.torre = t;
        this.vaga = vaga;
    }

    public int getNum() {
        return num;
    }

    public int getVaga() {
        return vaga;
    }

    public void setVaga(int vaga) {
        this.vaga = vaga;
    }

    public String toString(){
        return "ID: " + id + ", Numero do ap.: " + num + " Vaga: " + vaga + ",\nTorre:" + torre.toString();
    }
}

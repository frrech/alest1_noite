package trabalho.Trabalho1_Java;

public class FilaEspera {
    private class Node{
        private Apartamento ap;
        public Node next;
        public Node(Apartamento ap){
            this.ap = ap;
        }
        public Apartamento getAp() {
            return ap;
        }
    }

    public Node start;
    public Node end;
    public int size;

    public FilaEspera(){
        this.start = null;
        this.end = null;
        this.size = 0;
    }

    public void add(Apartamento ap){
        Node n = new Node(ap);
        if (start == null){
            start = n;
        }
        else{
            end.next = n;
        }
        end = n;
        size++;
    }

    public Apartamento remove(int vaga) throws Exception {
        if (start != null){
            Apartamento aux = start.getAp();
            aux.setVaga(vaga);
            start = start.next;
            if (start == null){
                end = null;
            }
            size--;
            return aux;
        }
        else{
            throw new Exception("Lista vazia");
        }
    }

    public void printQueue(){
        if (start != null){
            Node aux = start;
            int i = 0;
            while (aux != null) {
                System.out.println(i + " - " + aux.getAp().toString());
                aux = aux.next;
                i++;
            }

        }
        else{
            System.out.println("Lista vazia.");
        }
    }

    public boolean isEmpty(){
        return (start == null);
    }
}

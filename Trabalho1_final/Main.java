package trabalho.Trabalho1_Java;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws Exception {
        LinkedList<Apartamento> lista_vagas = new LinkedList<>();
        FilaEspera fila = new FilaEspera();
        Scanner sc = new Scanner(System.in);
        Scanner sc2 = new Scanner(System.in);
        Torre t = new Torre(1, "Alfa", "Osvaldo Cruz, n. 1");
        ArrayList<Torre> lista_torres = new ArrayList<>();

        lista_torres.add(t);

        int id_ap = 1;

        System.out.println("1) Adicionar ap\n2) Remover ap\n3) Listar vagas ocupadas\n4) Imprimir fila de espera\n5) Sair");
        int opcao = sc.nextInt();
        int nro_vagas = 10;

        while(opcao != 5) {
            switch (opcao) {
                case 1:
                    System.out.println("Digite o numero do apartamento: ");
                    int numero = sc.nextInt();
                    if(lista_vagas.size()<nro_vagas) {
                        System.out.println("Digite o numero da vaga: ");
                        int vaga = sc.nextInt();
                        if (isFree(vaga, lista_vagas)) {
                            System.out.println("1) Listar torres\n2) Selecionar torre (por ID)\n3) Adicionar nova torre\n4) Confirmar");
                            int opcao_torre = sc.nextInt();
                            Iterator<Torre> it = lista_torres.iterator();
                            while(opcao_torre != 4) {
                                switch (opcao_torre) {
                                    case 1:
                                        while (it.hasNext()) {
                                            System.out.println(it.next() + "\n");
                                        }
                                        break;
                                    case 2:
                                        System.out.println("Digite o ID da torre:");
                                        int torre_id = sc.nextInt();
                                        lista_vagas.add(new Apartamento(id_ap++, numero, lista_torres.get(torre_id), vaga));
                                        break;
                                    case 3:
                                        System.out.println("Digite o nome:");
                                        String nome = sc2.next();
                                        System.out.println("Digite o endereco:");
                                        String end = sc2.next();
                                        lista_torres.add(new Torre(lista_torres.size(), nome, end));
                                        break;

                                }
                                System.out.println("1) Listar torres\n2) Selecionar torre (por ID)\n3) Adicionar nova torre\n4) Confirmar");
                                opcao_torre = sc.nextInt();
                            }
                        } else {
                            System.out.println("Vaga ocupada");
                        }
                    }
                    else{
                        fila.add(new Apartamento(id_ap++, numero, t, -1));
                        System.out.println("Adicionado na fila de espera");
                    }
                    break;
                case 2:
                    System.out.println("Informe a vaga a ser liberada: ");
                    int vaga = sc.nextInt();
                    if(!isFree(vaga, lista_vagas)){
                        removeByVaga(vaga, lista_vagas);
                        if(!fila.isEmpty()){
                            lista_vagas.add(fila.remove(vaga));
                        }
                    } else {
                        System.out.println("Vaga livre");
                    }
                    break;
                case 3:
                    System.out.println(lista_vagas.toString());
                    break;
                case 4:
                    fila.printQueue();
                    break;
            }
            System.out.println("1) Adicionar ap\n2) Remover ap\n3) Listar vagas ocupadas\n4) Imprimir fila de espera\n5) Sair");
            opcao = sc.nextInt();
        }
    }

    public static boolean isFree(int vaga, LinkedList<Apartamento> l){
        if(!l.isEmpty()) {
            int i = 0;
            Apartamento a = l.get(i);
            while (a != null && i < l.size()) {
                if (a.getVaga() == vaga) {
                    return false;
                }
                a = l.get(i);
                i++;
            }
        }
        return true;
    }

    public static void removeByVaga(int vaga, LinkedList<Apartamento> l){
        int i = 0;
        Apartamento a = l.get(i);
        while(a != null && i < l.size()){
            if (a.getVaga() == vaga){
                l.remove(i);
            }
            a = l.get(i);
            i++;
        }
    }
}

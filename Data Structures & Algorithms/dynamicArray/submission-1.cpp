class DynamicArray {
    int* m_arr;
    int m_capacity;
    int m_index;
public:

    DynamicArray(int capacity):m_capacity(capacity),m_index(0) {
        m_arr = new int[capacity];
    }

    int get(int i) {
        if(!getSize()){
            return -1;
        }
        return m_arr[i];
    }

    void set(int i, int n) {
        m_arr[i] = n;
    }

    void pushback(int n) {
        if(getSize() == getCapacity()){
            resize();
        }
        m_arr[m_index++] = n;

    }

    int popback() {
        if(getSize() == 0){
            return -1;
        }
        if(!m_index){
            return m_arr[0];
        }
        return m_arr[--m_index];
    }

    void resize() {
        int* newArr = new int[getCapacity()*2];
        for(int i = 0; i < getSize();i++){
            newArr[i] = m_arr[i];
        }
        delete[] m_arr;
        m_capacity = getCapacity()*2;
        m_arr = newArr;

    }

    int getSize() {
        return m_index;
    }

    int getCapacity() {
        return m_capacity;
    }
};

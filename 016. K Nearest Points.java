


// Quick select to find K points(find Kth smallest element)
public static List<Point> quickFindPoints(int K, Point center, Point[] points) {
    quickSelect(K, points, center, 0, points.length - 1);
    List<Point> rs = new ArrayList<>();
    for (int i = 0; i < K; i++) {
        rs.add(points[i]);
    }
    return rs;
}

public static void quickSelect(int K, Point[] points, Point center, int start, int end) {
    Random rd = new Random();
    int pivot = rd.nextInt(end - start + 1) + start; 
    int i = start;
    int j = end - 1;
    double distance = getDistance(points[pivot], center);
    swap(points, pivot, end);
    while (i < j) {
        while (i < j && getDistance(points[i], center) <= distance) {
            i++;
        }
        while (i < j && getDistance(points[j], center) > distance) {
            j--;
        }
        swap(points, i, j);
    }
    swap(points, end, i);
    int amount = i - start + 1;
    if (K > amount) {
        quickSelect(K - amount, points, center, i + 1, end);
    } else if (K < amount) {
        quickSelect(K, points, center, start, i - 1);
    } else {
        return;
    }
}

public static void swap(Point[] points, int i, int j) {
    Point temp = points[i];
    points[i] = points[j];
    points[j] = temp;
}

public static double getDistance(Point A, Point B) {
    int xDistance = Math.abs(A.x - B.x);
    int yDistance = Math.abs(A.y - B.y);
    return Math.sqrt(Math.pow(xDistance, 2) + Math.pow(yDistance, 2));
}

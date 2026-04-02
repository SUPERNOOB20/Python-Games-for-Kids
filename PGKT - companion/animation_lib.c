

// The default is "sine"
void move((origin_x, origin_y), (destination_x, destination_y)) {
    return move_custom((origin_x, origin_y), (destination_x, destination_y), "sine");
}


void move_custom((origin_x, origin_y), (destination_x, destination_y), param) {
    if (param == "sine") {
        bezier_a = ;
        bezier_b = ;
    } else {
        bezier_a = param[0];
        bezier_b = param[1];
    }
    return ((next_x, next_y))
}
def calculate_dominant_offspring(dom_dom, dom_het, dom_rec, het_het, het_rec, rec_rec):
    d_d = dom_dom * 2 * 1
    d_h = dom_het * 2 * 1
    d_r = dom_rec * 2 * 1
    h_h = het_het * 2 * 0.75
    h_r = het_rec * 2 * 0.5
    r_r = rec_rec * 2 * 0

    total_dominant_offspring = d_d + d_h + d_r + h_h + h_r + r_r
    return total_dominant_offspring


dominant_offspring = calculate_dominant_offspring(17012, 18146, 16198, 19639, 18015, 17528)
print(dominant_offspring)

import sqlite3

def get_bouquets_for_occasion(occasion):
    """
    Look up which Aloure bouquets suit each occasion.

    ALWAYS call this when the customer asks what flowers or bouquet to buy,
    for any occasion: Birthday, Love, Anniversary, Congratulations,
    For Her, For Mom, I'm Sorry or Just Because.

    Args:
        occassion (str): The occassion

    Returns:
        list: (bouquet_id, occasion) pairs.
    """
    bouquet_occasion = occasion.capitalize()
    connection = sqlite3.connect("aloure_flowers.db")
    # response = connection.execute("SELECT * FROM bouquet_occasions WHERE occasion='occasion'")
    response = connection.execute("SELECT * FROM bouquet_occasions WHERE occasion = ? ",[bouquet_occasion])

    result = response.fetchall()
    print()
    # print("RESULT",result)
    print()
    connection.close()
    return result

# get_bouquets_for_occasion("birthday")





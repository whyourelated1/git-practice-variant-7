def share(amount, people):
    if people == 0:
        raise ValueError("people must not be zero")
    return amount / people

if __name__ == "__main__":
    print(share(1200, 3))


import numpy as np

# from PIL import Image

def conv_arr(inp: np.ndarray, ker: np.ndarray) -> np.ndarray:

    out = np.zeros_like(inp)

    if ker.size % 2 == 0:
        print("ker.size must be odd")
        return out

    inp_shift = ker.size // 2

    for out_index in range(out.size):

        sum = 0

        for ker_index in range(ker.size):

            inp_index = out_index - inp_shift + ker_index 

            if inp_index < 0:
                refl_inp_index = -inp_index
                if refl_inp_index < inp.size:
                    sum += inp[refl_inp_index] * ker[ker_index]

            elif inp_index >= inp.size:
                refl_inp_index = 2 * (inp.size - 1) - inp_index
                if refl_inp_index >= 0:
                    sum += inp[refl_inp_index] * ker[ker_index]
                
            else:
                sum += inp[inp_index] * ker[ker_index]

        out[out_index] = sum
    
    return out

def main():

    inp = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1])
    print("inp =", inp)

    ker = np.array([1, 2, 1])
    print("ker =", ker)

    out = conv_arr(inp, ker)
    print("out =", out)

if __name__ == "__main__":
    main()


import numpy as np
from PIL import Image

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

    ker = np.array([1, 2, 1])
    print("ker =", ker)

    img = Image.open('input.png').convert('L')
    arr = np.array(img)
    new_arr = np.zeros_like(arr)

    h, w = arr.shape

    for y in range(h):
        new_arr[y] = conv_arr(arr[y], ker)

    new_img = Image.fromarray(new_arr)
    new_img.show()
    new_img.save('output.png')

if __name__ == "__main__":
    main()


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


def check_mat_ker(ker: np.ndarray) -> bool:

    if ker.ndim != 2:
        print("ker must be 2D matrix")
        return False
    
    if ker.shape[0] != ker.shape[1]:
        print("ker must be square matrix")
        return False
    
    if ker.size % 2 == 0:
        print("ker.size must be odd")
        return False
    
    return True


def conv_mat(inp: np.ndarray, ker: np.ndarray) -> np.ndarray:

    out       = np.zeros_like(inp)
    shift_y   = ker.shape[0] // 2

    if not check_mat_ker(ker):
        return out

    for y in range(out.shape[0]):

        sum_arr = np.zeros_like(out[0])
        ker_y = 0

        for yy in range(y - shift_y, y + shift_y):

            if yy < 0:
                if -yy < out.shape[0]:
                    sum_arr += conv_arr(inp[-yy], ker[ker_y])

            elif yy >= out.shape[0]:
                    inp_y = 2 * (out.shape[0] - 1) - yy
                    if inp_y >= 0:
                        sum_arr += conv_arr(inp[inp_y], ker[ker_y])

            else:
                sum_arr += conv_arr(inp[yy], ker[ker_y])

            ker_y += 1

        out[y] = sum_arr
    
    return out


def main():

    ker = np.array([[1.2, 1.2, 1.2], 
                    [1.2,   0, 1.2], 
                    [1.2, 1.2, 1.2]])
    
    print("ker = \n", ker)

    img = Image.open('input.png').convert('L')
    mat = np.array(img)
    new_mat = conv_mat(mat, ker)

    new_img = Image.fromarray(new_mat)
    new_img.show()
    new_img.save('output.png')

if __name__ == "__main__":
    main()

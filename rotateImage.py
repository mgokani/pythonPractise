'''
write a function to rotate an image (2D matrix) by 90 degrees

image = [[1,2,3],
         [4,5,6],
         [7,8,9]]

output = [[1,4,7],
          [2,5,8],
          [3,6,9]]
'''

def rotateImage(image):
  n = len(image)
  m = len(image[0])

  for i in range(0, n):
    for j in range(i, m):
        temp = image[i][j]
        image[i][j] = image[j][i]
        image[j][i] = temp
  return image



if __name__ == "__main__":
  image = [[1,2,3], [4,5,6], [7,8,9]]
  print(rotateImage(image))

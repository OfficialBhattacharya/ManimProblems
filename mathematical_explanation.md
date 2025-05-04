# Mathematical Explanation: Correlation in Regular Polygons

## Correlation of Points on a Regular Polygon

A regular polygon with n sides can be represented in the complex plane as:

$$z_k = e^{2\pi i k/n} \text{ for } k = 0, 1, ..., n-1$$

When mapped to Cartesian coordinates, this gives:

$$x_k = \cos(2\pi k/n)$$
$$y_k = \sin(2\pi k/n)$$

### Key Properties

For any regular polygon with n ≥ 3 sides, the following properties hold:

1. The sum of the x-coordinates is zero:
   $$\sum_{k=0}^{n-1} \cos(2\pi k/n) = 0$$

2. The sum of the y-coordinates is zero:
   $$\sum_{k=0}^{n-1} \sin(2\pi k/n) = 0$$

3. The sum of the products of corresponding x and y coordinates is zero:
   $$\sum_{k=0}^{n-1} \cos(2\pi k/n) \sin(2\pi k/n) = 0$$

### Correlation Coefficient

The correlation coefficient between x and y coordinates is defined as:

$$\rho_{xy} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

Since $\bar{x} = \bar{y} = 0$ (from properties 1 and 2), this simplifies to:

$$\rho_{xy} = \frac{\sum x_i y_i}{\sqrt{\sum x_i^2 \sum y_i^2}}$$

From property 3, we know that $\sum x_i y_i = 0$, which means $\rho_{xy} = 0$.

Therefore, the correlation between x and y coordinates of vertices of any regular polygon is exactly zero.

## Regression Lines and Polygon Rotation

When a regular polygon is rotated by an angle θ, the new vertices are:

$$z_k(\theta) = e^{i\theta} \cdot e^{2\pi i k/n} = e^{i(\theta + 2\pi k/n)}$$

In Cartesian coordinates:

$$x_k(\theta) = \cos(\theta + 2\pi k/n)$$
$$y_k(\theta) = \sin(\theta + 2\pi k/n)$$

### Regression Line Behavior

The slope of the regression line is given by:

$$m = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2}$$

For a regular polygon, when it rotates by an angle θ, the regression line rotates by an angle θ/2.

This interesting property can be proven by examining how the covariance and variance of the coordinates change under rotation.

### Mathematical Proof

Let's define a rotation matrix for angle θ:

$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

When we apply this rotation to the vertices of a regular polygon, the resulting covariance matrix transforms in a way that causes the principal axis (which aligns with the regression line) to rotate at half the rate of the polygon.

This is related to the fact that when a set of points with zero correlation is rotated, the principal components of the distribution rotate at half the rate of the original points. 
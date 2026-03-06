# hello.exs

IO.puts("Hello, World!")

defmodule MathUtils do
  def sum_list(numbers) do
    Enum.reduce(numbers, 0, fn num, acc -> acc + num end)
  end
end

numbers = [1, 2, 3, 4, 5]
total = MathUtils.sum_list(numbers)
IO.puts("Sum of #{inspect(numbers)} = #{total}")
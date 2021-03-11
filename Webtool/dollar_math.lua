-- Specify delimiters for each type of output
function Math(m)
  -- For markdown->markdown cleaning
  if FORMAT:match "markdown" then
    if m.mathtype == "InlineMath" then
      return pandoc.RawInline('markdown', '\\( ' .. m.text .. ' \\)')
    else
      return pandoc.RawInline('markdown', '\n\\[' .. m.text .. '\\]\n')
    end
  end 

  -- For Latex and HTML output
  if FORMAT:match "latex" or FORMAT:match "pdf" then
    if m.mathtype == "InlineMath" then
      return m
      --return pandoc.RawInline('tex', '\\(' .. m.text .. '\\)')
    else
      if string.find(m.text, "label") then
        return pandoc.RawInline('tex', '\n\\begin{equation}'.. m.text .. '\\end{equation}\n')
      else
        return pandoc.RawInline('tex', '\n\\begin{align*}'.. m.text .. '\\end{align*}\n')
      end
    end
  end 

  if FORMAT:match "html" or FORMAT:match "html5" then
    if m.mathtype == "InlineMath" then
      return m
    else
      return pandoc.RawInline('html', '\n<span class="math display">\n\\begin{align*}'.. m.text .. '\\end{align*}\n<span>')
    end
  end 

end


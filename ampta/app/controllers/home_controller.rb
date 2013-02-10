class HomeController < ApplicationController
  before_filter :sidenav
  
  def index
   # @users = User.all
  end

end
